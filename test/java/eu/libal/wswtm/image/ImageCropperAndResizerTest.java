package eu.libal.wswtm.image;

import org.junit.Before;
import org.junit.Test;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.Is.is;


/**
 *
 */
public class ImageCropperAndResizerTest {

    private ImageCropperAndResizer cropAndResize;

    @Before
    public void setup() {
        cropAndResize = new ImageCropperAndResizer();
    }

    @Test
    public void shouldReturnOnlyTheSelectedPortionOfThePixels() throws IOException {
        File input = new File("resources/classes/calibration/bw_20_by_20.png");
        BufferedImage bufferedImage = ImageIO.read(input);

        PixelData crop = cropAndResize.crop(bufferedImage, 10, 10, 5, 5);

        assertThat(crop.getPixelData().length, is(25));
        assertThat(crop.getPixelData()[0], is(new int[] { 0, 0, 0 }));
        assertThat(crop.getPixelData()[24], is(new int[] { 0, 0, 0 }));
    }
}