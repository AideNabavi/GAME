import qrcode

wallet_address = "0x021891D60B3569a859927708e9347ebe02021556"

qr = qrcode.make(wallet_address)
qr.save("./donation_qr.png")