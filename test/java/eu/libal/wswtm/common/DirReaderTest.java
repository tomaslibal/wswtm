package eu.libal.wswtm.common;

import org.junit.Test;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

public class DirReaderTest {

    @Test
    public void shouldReturnAListOfFilesInTheDirectory() {
        File parent = new File(this.getClass().getResource("/reader").getPath());
        Optional<List<File>> files = DirReader.getDirFiles(parent);
        List<File> expected = new ArrayList<>();
        expected.add(new File(this.getClass().getResource("/reader/bar.md").getFile()));
        expected.add(new File(this.getClass().getResource("/reader/foo.txt").getFile()));

        assertThat(files.isPresent(), is(true));
        assertThat(files.get(), is(expected));
    }

    @Test
    public void shouldReturnEmptyOptionalIfParentDoesNotExist() {
        File parent = new File("/foo/bar");
        Optional<List<File>> files = DirReader.getDirFiles(parent);

        assertThat(files, is(Optional.empty()));
    }
}