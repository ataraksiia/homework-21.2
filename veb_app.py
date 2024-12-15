def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type=text/html")
    self.end_headers()
    with open("pages/contacts.html", "p", encoding="utf-8") as file:
        page = file.read()
    self.wfile.write(bytes(page, "utf-8"))
