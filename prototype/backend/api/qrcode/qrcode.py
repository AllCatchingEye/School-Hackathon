from flask import Blueprint, jsonify, request
from app import db
from models.hackathon import Hackathon as Hackathonmodel
from models.token import Token as Tokenmodel
from utils.user_roles import auth_required, Config
import qrcode
import base64
import FPDF

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

QRCode = Blueprint('qrcode', __name__)

@QRCode.route('/<hackathonid>/', methods=["GET"])
@auth_required([Config.TEACHER_ID, Config.ADMIN_ID])
def create_qrcode(hackathonid):

    #query here to get tokenid and slug
    result = db.session.query(Tokenmodel.tokenid, Hackathonmodel.slug).join(Hackathonmodel).filter(Hackathonmodel.hackathonid==hackathonid).all()
    
    #concat here
    qr = qrcode.QRCode()
    for i in result:    
        tokenid = i[0]
        slug = i[1]
        url = slug + "/" + tokenid
        
        qr.add_data(url)
        qr.make(fit = True)
        img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
        #b64 = base64.b64encode(img).decode("utf-8")

        #output = 'test.pdf'
        #pdf = FPDF()
        #pdf.add_page()
        #pdf.image(img)
        #pdf.output(output)

    #img.save("wirfuerschule2.png")
    return "Nix"

