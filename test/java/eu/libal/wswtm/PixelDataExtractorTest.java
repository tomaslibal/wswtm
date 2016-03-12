package eu.libal.wswtm;

import org.junit.Before;
import org.junit.Test;

import java.io.File;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

/**
 *
 */
public class PixelDataExtractorTest {

    private PixelDataExtractor extractor;

    @Before
    public void setup() {
        extractor = new PixelDataExtractor();
    }

    @Test
    public void shouldExtractPixelsAsAnArrayOfIntValues() {

        File rgbw_2_by_2 = new File("resources/classes/calibration/rgbw_2_by_2.png");
        PixelData pixelData = extractor.extract(rgbw_2_by_2);

        assertThat(pixelData.getPixelData().length, is(4));

        assertThat(pixelData.getPixelData()[0], is(new int[] { 255, 0, 0 }));
        assertThat(pixelData.getPixelData()[1], is(new int[] { 0, 0, 255 }));
        assertThat(pixelData.getPixelData()[2], is(new int[] { 0, 255, 0 }));
        assertThat(pixelData.getPixelData()[3], is(new int[] { 255, 255, 255 }));
    }
}