import qrcode
from PIL import Image

def criar_qr_code(uri, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    # Endereço Bitcoin para receber pagamentos
    endereco = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    
    # URI de pagamento Bitcoin com o endereço e o valor
    uri = f"bitcoin:{endereco}?amount=0.0001"
    
    # Nome do arquivo para salvar o QR code
    filename = "qr_code.png"
    
    # Cria o QR code e salva como imagem
    criar_qr_code(uri, filename)
    
    print("QR code gerado com sucesso como:", filename)
    print("Endereço Bitcoin para receber pagamentos:", endereco)
