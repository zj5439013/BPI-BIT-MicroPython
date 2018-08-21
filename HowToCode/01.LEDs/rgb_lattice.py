from display import BpiBitNeoPixel, NeoPixelPower
NeoPixelPower(True)
View = BpiBitNeoPixel()

RGB = (10, 10, 10)
View.LoadXY(2, 2, RGB)
View.Show()
