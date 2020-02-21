import utilities

def rotate_90_degrees(image_array, direction = 1):
    '''
    This function rotates an image, given the list representation of the image and the intended direction
    (list, int)-> (list)
    >>>rotate_90_degrees([[3,4,5],[3,5,5], [2,3,4]], 1)
    [[2,3,3],[3,5,4],[4,5,5]]
    '''
    answer = list()
    if direction == 1:
	    for i in range(len(image_array)):
		    value = list()
		    for j in range(len(image_array[i])-1,-1,-1):
			    value.append(image_array[j][i])
		    answer.append(value)
    else:
	    for i in range(len(image_array)-1,-1,-1):
		    value = list()
		    for j in range(len(image_array[i])):
			    value.append(image_array[j][i])
		    answer.append(value)	
    return answer

def flip_image(image_array, axis = 0):
    '''
    This function rotates an image, given the list representation of the image and the intended direction
    (list, int)-> (list)
    >>>flip_image([[3,4,5],[3,5,5], [2,3,4]], 0)
    [[2,3,3],[3,5,4],[4,5,5]]
    '''    
    answer = list()
    if axis == 0:
	    for i in range(len(image_array)):
		    value = list()
		    for j in range(len(image_array)-1,-1,-1):
			    value.append(image_array[i][j])
		    answer.append(value)
    elif axis == 1:
	    for i in range(len(image_array)-1,-1,-1):
		    answer.append(image_array[i])
    elif axis == -1:
	    for i in range(len(image_array)-1,-1,-1):
		    value = list()
		    for j in range(len(image_array)-1-1,-1):
			    value.append(image_array[j][i])
		    answer.append(value)
    else: 
	    return 0
    return answer
	         

	         
def crop(image_array,direction,n_pixels):
    '''
    This function rotates an image, given the list representation of the image and the intended direction
    (list, int)-> (list)
    >>>flip_image([[3,4,5],[3,5,5], [2,3,4]], 0)
    [[2,3,3],[3,5,4],[4,5,5]]
    '''     
    if direction == 'left':
            value = list()
            for j in range(len(image_array)):
                    value.append(image_array[j][n_pixels:])
    elif direction == 'up':
	    value = image_array[n_pixels:]
    elif direction == 'right':
            value = list()
            for j in range(len(image_array)):
                    value.append(image_array[j][:-n_pixels])    
    elif direction == 'down':
            value = image_array[:-n_pixels]
    return value
def invert_grayscale(image_array):
    '''
    This function rotates an image, given the list representation of the image and the intended direction
    (list, int)-> (list)
    >>>flip_image([[3,4,5],[3,5,5], [2,3,4]])
    [[2,3,3],[3,5,4],[4,5,5]]
    '''     
    answer = list()
    for i in range(len(image_array)):
	    value = list()
	    for j in range(len(image_array[i])): 
		    value.append(255 - image_array[i][j])
	    answer.append(value)
    return answer
def rgb_to_grayscale(rgb_image_array):
    '''
    This function rotates an image, given the list representation of the image and the intended direction
    (list, int)-> (list)
    >>>flip_image([[3,4,5],[3,5,5], [2,3,4]])
    [[2,3,3],[3,5,4],[4,5,5]]
    '''     
    answer = list()
    for i in range(len(rgb_image_array)):
	    value = list()
	    for j in range(len(rgb_image_array[i])):
		    value.append(rgb_image_array[i][j][0]* 0.2989 + rgb_image_array[i][j][1]* 0.5870 + rgb_image_array[i][j][2]* 0.1140)
	    answer.append(value)
    return answer
def invert_rgb(image_array):
    '''
    This function rotates an image, given the list representation of the image and the intended direction
    (list, int)-> (list)
    >>>flip_image([[3,4,5],[3,5,5], [2,3,4]])
    [[2,3,3],[3,5,4],[4,5,5]]
    '''     
    answer = list()
    for i in range(len(image_array)):
	    value = list()
	    for j in range(len(image_array[i])):    
		    value.append([255 - image_array[i][j][0], 255 - image_array[i][j][1], 255 - image_array[i][j][2]])
	    answer.append(value)
    return answer

def histogram_equalization(image_array):
    '''
    This function rotates an image, given the list representation of the image and the intended direction
    (list, int)-> (list)
    >>>flip_image([[3,4,5],[3,5,5], [2,3,4]])
    [[2,3,3],[3,5,4],[4,5,5]]
    '''     
    answer = list()
    minimum = 125
    pmf = [0]*256
    total_length = len(image_array)
    total_width = len(image_array[0])
    for i in range(total_length): 
	    for k in range(total_width):
	            pmf[round(image_array[i][k])] += 1
	    if min(image_array[i]) > minimum:
		    minimum = round(min(image_array[i]))
    for i in range(total_length):
	    value = list()
	    for j in range(total_width):
		    value.append(round((sum(pmf[0:round(image_array[i][j]+1)]) - pmf[minimum])/(total_length * total_width - pmf[minimum]) * 255))
	    answer.append(value)
    return answer
if (__name__ == "__main__"):
    file = 'surprised_pikachu.png'
    utilities.write_image(rgb_to_grayscale(utilities.image_to_list(file)), 'gray.png')
    

