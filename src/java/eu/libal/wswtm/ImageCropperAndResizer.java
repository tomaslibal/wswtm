package eu.libal.wswtm;

import java.awt.image.BufferedImage;

/**
 *
 */
public class ImageCropperAndResizer {

    public ImageCropperAndResizer() {

    }

    public PixelData cropCenter(BufferedImage img, int w, int h) {
        return crop(img, Math.round( img.getWidth() / 2 ), Math.round( img.getHeight() / 2 ), w, h);
    }

    public PixelData crop(BufferedImage img, int x, int y, int w, int h) {
        return null;
    }
}
