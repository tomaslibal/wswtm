package eu.libal.wswtm.common;

import java.io.File;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class DirReader {

    public static Optional<List<File>> getDirFiles(File parent) {
        if (parent.exists()) {
            Stream<File> stream = Arrays.stream(parent.listFiles());
            return Optional.of(stream.collect(Collectors.toList()));
        }

        return Optional.empty();
    }
}
