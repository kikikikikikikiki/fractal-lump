import imageio
images = []
filenames = []
s = 1
while s<10:
    filenames.append('image000'+ str(s) +'.jpg')
    s += 1
while s<100:
    filenames.append('image00'+ str(s) +'.jpg')
    s += 1
while s<1000:
    filenames.append('image0'+ str(s) +'.jpg')
    s += 1
while s<10000:
    filenames.append('image'+ str(s) +'.jpg')
    s += 1

#for filename in filenames:
    #images.append(imageio.imread(filename))
#imageio.mimsave('movie.gif', images)
#mim = mimread('~/image0001.jpg)
with imageio.get_writer('movie.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
