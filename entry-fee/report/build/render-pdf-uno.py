# CONTEXT: $100B ENTRY FEE v5 — render the docx to PDF with the Contents index updated (LibreOffice UNO).
import subprocess, time, sys, os, uno
from com.sun.star.beans import PropertyValue
SRC = os.path.abspath(sys.argv[1]); OUT = os.path.abspath(sys.argv[2])
prof = "/tmp/lo_uno_profile"
p = subprocess.Popen(["soffice", f"-env:UserInstallation=file://{prof}", "--headless", "--invisible", "--norestore",
                      "--accept=socket,host=127.0.0.1,port=2002;urp;"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
ctx = None
for _ in range(60):
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        ctx = resolver.resolve("uno:socket,host=127.0.0.1,port=2002;urp;StarOffice.ComponentContext"); break
    except Exception:
        time.sleep(1)
if ctx is None: print("no UNO connection"); p.kill(); sys.exit(1)
desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
def pv(n, v):
    x = PropertyValue(); x.Name = n; x.Value = v; return x
doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(SRC), "_blank", 0, (pv("Hidden", True),))
idx = doc.getDocumentIndexes()
for i in range(idx.getCount()):
    idx.getByIndex(i).update()
doc.refresh()
doc.storeToURL(uno.systemPathToFileUrl(OUT), (pv("FilterName", "writer_pdf_Export"),))
doc.close(True)
try: desktop.terminate()
except Exception: pass
p.wait(timeout=30)
print("PDF written", OUT, os.path.getsize(OUT), "bytes; indexes updated:", idx.getCount())
