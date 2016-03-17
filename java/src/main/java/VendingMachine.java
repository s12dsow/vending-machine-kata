import java.util.ArrayList;
import java.util.HashMap;

public class VendingMachine {
    Integer currentAmount;
    Integer returnCoins;
    String displayMessage;
    HashMap<String, ArrayList<Integer>> products;

    public VendingMachine(){
        currentAmount = 0;
        returnCoins = 0;
        displayMessage = "";

        products = new HashMap<>();


//        products.put("Cola", 100);
//        products.put("Chips", 50);
//        products.put("Candy", 65);
    }

    public void acceptCoins(Integer coinInput) {
        if (coinInput == 1) {
            returnCoins += coinInput;
        }

        Integer[] coins = {5, 10, 25};

        for (Integer item: coins) {
            if (coinInput.equals(item)) {
                currentAmount += item;
            }
        }
    }

    public String selectProduct(String item) {
        String product = "";

        Integer price = products.get(item);

        if (currentAmount.equals(price)) {
            if (products.containsKey(item)) {
                product = item;
                currentAmount -= price;
                displayMessage = "THANK YOU";
            }
        } else if (currentAmount > price) {
            if (products.containsKey(item)) {
                product = item;
                returnCoins += currentAmount - price;
                currentAmount -= price;
                displayMessage += "THANK YOU";
            }
        } else {
            displayMessage = String.format("PRICE: %d", price);
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
