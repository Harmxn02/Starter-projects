package inventory;

import java.util.ArrayList;

public class Inventory {
    private final ArrayList<Product> products;

    public Inventory(ArrayList<Product> products) {
        this.products = products;
    }

    public ArrayList<Product> getProducts() {
        return products;
    }

    double getInventoryValue() {
        double totalValue = 0;
        for (Product product : products){
            totalValue += product.getTotalPrice();
        }

        return totalValue;
    }
}
