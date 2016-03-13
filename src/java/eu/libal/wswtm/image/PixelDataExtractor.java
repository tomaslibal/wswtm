package eu.libal.wswtm.image;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

/**
 *
 */
public class PixelDataExtractor {

    public PixelDataExtractor() {

    }

    /**
     * Column by column pixel data
     *
     * @param input
     * @return
     */
    public PixelData extract(File input) {
        PixelData pd = new PixelData();
        int[][] bitmapArray;
        BufferedImage bitmapImg;

        try {
            bitmapImg = ImageIO.read(input);

            bitmapArray = new int[bitmapImg.getHeight() * bitmapImg.getWidth()][3];
            int[] rgbComponent;

            int counter = 0;

            int i = 0;
            for (int x = 0; x < bitmapImg.getWidth(); x++) {
                for (int y = 0; y < bitmapImg.getHeight(); y++) {
                    rgbComponent = getRGBComponent(bitmapImg, x, y);

                    bitmapArray[i][0] = rgbComponent[0];
                    bitmapArray[i][1] = rgbComponent[1];
                    bitmapArray[i][2] = rgbComponent[2];

                    i++;
                }
            }


            pd.setPixelData(bitmapArray);
            return pd;
        } catch (IOException e) {
            e.printStackTrace();
        }

        return pd;
    }

    private int[] getRGBComponent(BufferedImage bitmapImg, int x, int y) {

        Color color = new Color(bitmapImg.getRGB(x, y));

        int[] rgb = {
                color.getRed(),
                color.getGreen(),
                color.getBlue(),
                color.getAlpha()
        };

        return rgb;
    }

}
