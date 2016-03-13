package eu.libal.wswtm.image;

import java.awt.*;
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
        PixelData data = new PixelData();
        int[][] pixels = new int[w*h][3];
        //int[] pixels1D = new int[w*h];

        //img.getRGB(Math.round(x - (w / 2)), Math.round(y - (h / 2)), w, h, pixels1D, 0, 1);

        int startX = Math.round(x - (w / 2));
        int startY = Math.round(y - (h / 2));

        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                Color color = new Color(img.getRGB(i + startX, j + startY));
                pixels[i*j] = new int[] { color.getRed(), color.getGreen(), color.getBlue() };
            }
        }

        data.setPixelData(pixels);

        return data;
    }
}
