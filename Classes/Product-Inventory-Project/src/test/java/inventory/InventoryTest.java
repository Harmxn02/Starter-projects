package inventory;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class InventoryTest {
    @Test
    void testSumInventoryValue() {
        // Arrange
        Product p1 = new Product(10.00, 1, 5);
        Product p2 = new Product(7.50, 2, 3);
        Product p3 = new Product(5.00, 3, 2);

        ArrayList<Product> products = new ArrayList<>();
        products.add(p1);
        products.add(p2);
        products.add(p3);

        Inventory inventory = new Inventory(products);

        // Act
        double expectedTotalValue = 82.50;
        double actualTotalValue = inventory.getInventoryValue();

        // Assert
        assertEquals(expectedTotalValue, actualTotalValue);
    }
}