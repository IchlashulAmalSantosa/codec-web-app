import cv2

def compress_image(input_path, output_path, quality=50):
    image = cv2.imread(input_path)
    cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    return output_path
