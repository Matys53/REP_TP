package org.example;

import java.util.Random;

public class Main {

    public static void main(String[] args) {
        int iterations = 1000000;
        int validCount = 0;

        Random random = new Random();

        // Range : -1000 ; 1000
        for (int i = 0; i < iterations; i++) {
            float x = random.nextFloat() * 2e3f - 1e3f;
            float y = random.nextFloat() * 2e3f - 1e3f;
            float z = random.nextFloat() * 2e3f - 1e3f;

            float leftSide = (x + y) + z;
            float rightSide = x + (y + z);

            if (leftSide - rightSide == 0) {
                validCount++;
            }
        }

        double percentageValid = (validCount * 100.0) / iterations;
        System.out.println("Pourcentage d'égalités valides : " + percentageValid + "% ");
    }

}
