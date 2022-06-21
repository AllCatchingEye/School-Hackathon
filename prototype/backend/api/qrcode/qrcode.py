from flask import Blueprint, jsonify, request
from app import db
from models.hackathon import Hackathon as Hackathonmodel
from models.token import Token as Tokenmodel
from utils.user_roles import auth_required, Config
from utils.pdf import PDF
import qrcode
import base64
import io

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

QRCode = Blueprint('qrcode', __name__)

@QRCode.route('/<hackathonid>/', methods=["GET"])
@auth_required([Config.TEACHER_ID, Config.ADMIN_ID])
def create_qrcode(hackathonid):

    result = db.session.query(Tokenmodel.tokenid, Hackathonmodel.slug).join(Hackathonmodel).filter(Hackathonmodel.hackathonid==hackathonid).all()
    
    j = 0
    for i in result:
        j = j+1
        tokenid = i[0]
        slug = i[1]
        url = slug + "/" + tokenid
        
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make(fit = True)
        img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        #img_str = base64.b64encode(buffered.getvalue()).decode("utf-8").encode()
        fname = "wirfuerschule{0}.png".format(j)
        img.save(fname)
        #p = PDF()
        #p.add_page()
        #pdf.add_image(img)
        #p.sample_pdf(img_str, fname, p)
    return "Nix"

