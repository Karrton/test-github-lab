package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MainTest {
    @Test
    public void testAdd() {
        assertEquals(5, Main.add(2, 3));
    }

    @Test
    public void testSubtract() {
        assertEquals(3, Main.subtract(5, 2));
        assertEquals(-1, Main.subtract(2, 3));
    }

    @Test
    public void testMultiply() {
        assertEquals(6, Main.multiply(2, 3));
        assertEquals(0, Main.multiply(5, 0));
        assertEquals(-10, Main.multiply(2, -5));
    }
}