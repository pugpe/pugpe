# -*- coding:utf-8 -*-
import os

from StringIO import StringIO

from django.conf import settings
from django.db.models.fields.files import ImageFieldFile

from reportlab.lib.pagesizes import landscape, B5
from reportlab.platypus import BaseDocTemplate, PageTemplate, Paragraph
from reportlab.platypus import Image, Frame, FrameBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import utils
from reportlab.lib.enums import TA_CENTER


def get_image(image, width=1*cm):
    img = utils.ImageReader(image)
    iw, ih = img.getSize()
    aspect = ih / float(iw)

    if isinstance(image, ImageFieldFile):
        image.seek(0)
    return Image(image, width=width, height=(width * aspect))


def generate(name, event):
    '''
    Retona pdf em memória (StringIO)

    name -- Nome do participante
    event -- Instância de event
    '''
    img_path = os.path.join(settings.PROJECT_ROOT, 'static_files/img/cert/')

    frame_header = Frame(x1=0, y1=0,  width=700, height=460)
    frame_body = Frame(x1=100, y1=0,  width=500, height=300)
    frame_sign = Frame(x1=50, y1=0,  width=300, height=130)
    frame_logo = Frame(x1=400, y1=0,  width=300, height=130)

    mainPage = PageTemplate(
        frames=[frame_header, frame_body, frame_sign, frame_logo],
    )


    dest = StringIO()
    doc = BaseDocTemplate(
        dest, pageTemplates=mainPage, pagesize=landscape(B5),
        rightMargin=72,leftMargin=72, topMargin=72,bottomMargin=18,
    )


    cert = []
    cert.append(get_image(os.path.join(img_path, 'logo2.png'), 5*cm))

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('Body2', leading=22))
    styles.add(ParagraphStyle('NormalCenter', alignment=TA_CENTER))

    cert.append(
        Paragraph(u'<font size=25>Certificado de Participação</font>',
        styles['Title']),
    )

    cert.append(FrameBreak())

    text = (u'Certificamos que <b>{name}</b> participou do '
            u'Encontro do {event}, '
            u'no dia {date}, '
            u'realizado em {local} com carga horária de {len} horas, '
            u'na qualidade de <b>participante</b>.')
    text = text.format(
        name=name, event=event, local=event.location, len=event.length,
        date=event.date.strftime('%d/%m/%Y'),
    )

    cert.append(
        Paragraph(u'<font size=16.0>{0}</font>'.format(text), styles['Body2']),
    )

    cert.append(FrameBreak())

    cert.append(get_image(event.signature.signature, 7*cm))
    cert.append(Paragraph(
        u'_' * len(event.signature.name), styles['NormalCenter']),
    )
    cert.append(
        Paragraph(u'{0}'.format(event.signature.name), styles['NormalCenter']),
    )
    cert.append(
        Paragraph(u'{0}'.format(event.signature.title),
        styles['NormalCenter']),
    )
    cert.append(FrameBreak())

    cert.append(Paragraph(u'<b>Realização</b>', styles['NormalCenter']))
    cert.append(get_image(os.path.join(img_path, 'logo_pug.jpg'), 7*cm))

    doc.build(cert)
    dest.seek(0)
    return dest
