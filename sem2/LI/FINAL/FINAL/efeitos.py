from PIL import Image 
from PIL import ExifTags 
from PIL import ImageFilter
import sys
import math 

def trocaDeCor(fname):
	im = Image.open(fname)
	width, height = im.size
	
	new_im = Image.new(im.mode, im.size)
	
	for x in range(width):
		for y in range(height):
			p = im.getpixel( (x,y) )
			r = p[1]
			g = p[0]
			b = p[2]
			new_im.putpixel((x,y), (r, g, b) )
	new_im.save(fname)


def tonDeCinza(fname):
	im = Image.open(fname)
	new_im = im.convert("L")

		
	width, height = im.size
	new_im = Image.new("L", im.size)
	
	for x in range(width):
		for y in range(height):
			p = im.getpixel( (x,y) )
			l = int(p[0]*0.299 + p[1]*0.587 + p[2]*0.144)
			new_im.putpixel( (x,y), (l) )
	new_im.save(fname)


def intensidade(fname):
	im = Image.open(fname)
	
	new_im = im.convert("YCbCr")
	width, height = im.size
	
	for x in range(width):
		for y in range(height):
			pixel = new_im.getpixel( (x,y) )
			py = min(255, int(pixel[0] * float(2) )) # [0] is the Y channel
			new_im.putpixel( (x,y), (py, pixel[1], pixel[2]) )
	new_im.save(fname)


def blur(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.BLUR)
	im1.save(fname)
	
def contour(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.CONTOUR)
	im1.save(fname)

def detail(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.DETAIL)
	im1.save(fname)

def edgeEnhance(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.EDGE_ENHANCE)
	im1.save(fname)

def edgeEnhanceMore(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
	im1.save(fname)
	
def emboss(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.EMBOSS)
	im1.save(fname)
	
def findEdges(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.FIND_EDGES)
	im1.save(fname)
	
def sharpen(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.SHARPEN)
	im1.save(fname)

def smooth(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.SMOOTH)
	im1.save(fname)
	
def smoothMore(fname):
	
	im = Image.open(fname)
	im1 = im.filter(ImageFilter.SMOOTH_MORE)
	im1.save(fname)
