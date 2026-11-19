import tempfile, unittest
from pathlib import Path
from PIL import Image
from main import compare_images
class PixelDiffTests(unittest.TestCase):
    def test_identical_images(self):
        with tempfile.TemporaryDirectory() as tmp:
            a=Path(tmp)/"a.png"; b=Path(tmp)/"b.png"
            Image.new("RGB",(4,4),"white").save(a); Image.new("RGB",(4,4),"white").save(b)
            report=compare_images(a,b,Path(tmp)/"out")
            self.assertEqual(report["changed_pixels"],0)
    def test_changed_pixel(self):
        with tempfile.TemporaryDirectory() as tmp:
            a=Path(tmp)/"a.png"; b=Path(tmp)/"b.png"
            Image.new("RGB",(3,3),"white").save(a); im=Image.new("RGB",(3,3),"white"); im.putpixel((1,1),(0,0,0)); im.save(b)
            report=compare_images(a,b,Path(tmp)/"out",8)
            self.assertEqual(report["changed_pixels"],1)
if __name__=="__main__": unittest.main()
