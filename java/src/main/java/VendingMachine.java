import java.util.HashMap;

public class VendingMachine {
    Integer currentAmount;
    Integer returnCoins;
    String displayMessage;
    HashMap<String, Integer> products;

    public VendingMachine(){
        currentAmount = 0;
        returnCoins = 0;
        displayMessage = "";

        products = new HashMap<>();
        products.put("Cola", 100);
        products.put("chips", 50);
        products.put("candy", 65);
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

    public String display() {
        if (currentAmount > 0) {
            displayMessage = String.format("Current Amount: %d", currentAmount);
        }
        else {
            displayMessage = "INSERT COINS";
        }
        return displayMessage;
    }

}
