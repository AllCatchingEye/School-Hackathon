from flask import Blueprint, send_file
from app import db
from models.hackathon import Hackathon as Hackathonmodel
from models.token import Token as Tokenmodel
from utils.user_roles import auth_required, Config
from datetime import datetime
from fpdf import FPDF
import qrcode
import time
import os


from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

QRCode = Blueprint('qrcode', __name__)

@QRCode.route('/<hackathonid>/', methods=["GET"])
@auth_required([Config.TEACHER_ID, Config.ADMIN_ID])
def create_qrcode(hackathonid):

    result = db.session.query(Tokenmodel.tokenid, Hackathonmodel.slug).join(Hackathonmodel).filter(Hackathonmodel.hackathonid==hackathonid).all()
    
    j = 0
    suffix_png = ".png"
    suffix_pdf = ".pdf"
    p = FPDF('P', 'mm', 'A4')
    p.set_font('Arial', 'B', 16)

    current_time = time.time()
    date_time = datetime.fromtimestamp(current_time)
    tstamp = date_time.strftime("%Y%m%d%H%M%S")

    for i in result:
        j = j+1
        tokenid = i[0]
        slug = i[1]
        url = "https://wirfuerschule.lio.codes/submission/" + slug + "/" + tokenid
        
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make(fit = True)
        img = qr.make_image()
        fname = "wirfuerschule{0}{1}".format(j, suffix_png)
        img.save(fname)

        p.add_page()
        p.cell(100, 40, 'QRCode ID: {0}'.format(tokenid))
        p.image(fname, x=70, y=100, w=80, h=80)
        os.remove(fname)

    pdffile = "wirfuerschule{0}{1}".format(tstamp, suffix_pdf)
    p.output(pdffile)
    data = send_file(pdffile, mimetype = 'pdf', attachment_filename = pdffile, as_attachment = True)
    os.remove(pdffile)
    return data
