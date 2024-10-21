package org.example;

import java.util.Random;

public class Main {

    public static void main(String[] args) {
        int iterations = 1000000;
        int validCount = 0;

        Random random = new Random();

        // Range : -1000 ; 1000
        for (int i = 0; i < iterations; i++) {
            double x = random.nextFloat() * 2e3f - 1e3f;
            double y = random.nextFloat() * 2e3f - 1e3f;
            double z = random.nextFloat() * 2e3f - 1e3f;

            double leftSide = (x + y) + z;
            double rightSide = x + (y + z);

            if (leftSide - rightSide == 0) {
                validCount++;
            }
        }

        double percentageValid = (validCount * 100.0) / iterations;
        System.out.println(String.format("%.2f", percentageValid));
    }

}
