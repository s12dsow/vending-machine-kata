import java.util.ArrayList;
import java.util.HashMap;

public class VendingMachine {
    Integer currentAmount;
    Integer returnCoins;
    String displayMessage;
    HashMap<String,Integer> products;
    HashMap<String, Integer> productsQuantity;
    HashMap<Integer, Integer> coinQuantity;

    public VendingMachine(){
        currentAmount = 0;
        returnCoins = 0;
        displayMessage = "";

        products = new HashMap<>();
        products.put("Cola", 100);
        products.put("Chips", 50);
        products.put("Candy", 65);

        productsQuantity = new HashMap<>();
        productsQuantity.put("Cola", 5);
        productsQuantity.put("Chips", 10);
        productsQuantity.put("Candy", 15);

        coinQuantity = new HashMap<>();
        coinQuantity.put(25, 5);
        coinQuantity.put(10, 10);
        coinQuantity.put(5, 10);
    }

    public void acceptCoins(Integer coinInput) {
        if (coinInput == 1) {
            returnCoins += coinInput;
        }
        Integer[] coins = {5, 10, 25};

        for (Integer item: coins) {
            if (coinInput.equals(item)) {
                currentAmount += item;
                coinQuantity.put(item, coinQuantity.get(item) + 1);
            }
        }
    }

    public String selectProduct(String item) {
        String product = "";

        Integer price = products.get(item);
        Integer quantity = productsQuantity.get(item);

        if (canMakeChange()) {
            if (quantity > 0) {
                if (currentAmount.equals(price)) {
                    if (products.containsKey(item)) {
                        product = item;
                        currentAmount -= price;
                        productsQuantity.put(item, productsQuantity.get(item) - 1);
                        displayMessage = "THANK YOU";
                    }
                } else if (currentAmount > price) {
                    if (products.containsKey(item)) {
                        product = item;
                        returnCoins += currentAmount - price;
                        currentAmount -= price;
                        productsQuantity.put(item, productsQuantity.get(item) - 1);
                        displayMessage = "THANK YOU";
                    }
                } else {
                    displayMessage = String.format("PRICE: %d", price);
                }
            } else {
                displayMessage = "OUT OF STOCK";
            }
        } else {
            displayMessage = "EXACT CHANGE ONLY";
        }
        return product;
    }

    public void refundCoins() {
        returnCoins += currentAmount;
        currentAmount = 0;
    }
    public Integer returnCoins() {
        return returnCoins;
    }

    public boolean canMakeChange() {
        boolean statement = false;
        if (coinQuantity.get(10) > 1 && coinQuantity.get(5) > 1 || coinQuantity.get(5) > 3) {
            statement = true;
        }
        return statement;
    }

    public String display() {
        if (!displayMessage.isEmpty()) {
            String msg = displayMessage;
            displayMessage = "";
           return msg;
        } else if (currentAmount > 0) {
            displayMessage = String.format("Current Amount: %d", currentAmount);
        }
        else {
            displayMessage = "INSERT COINS";
        }
        return displayMessage;
    }
}
