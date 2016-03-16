import org.junit.Before;
import org.junit.Test;

import java.util.HashMap;

import static org.junit.Assert.*;

public class VendingMachineTest {
    private VendingMachine vendingMachine;

    @Before
    public void setUp() throws Exception {
        vendingMachine = new VendingMachine();
    }

    @Test
    public void vendingMachineAcceptsQuarters() {
        vendingMachine.acceptCoins(25);

        assertEquals(vendingMachine.currentAmount, (Integer) 25);
    }
    @Test
    public void vendingMachineAcceptsDimes() {
        vendingMachine.acceptCoins(10);

        assertEquals(vendingMachine.currentAmount, (Integer) 10);
    }
    @Test
    public void vendingMachineAcceptsNickels() {
        vendingMachine.acceptCoins(5);

        assertEquals(vendingMachine.currentAmount, (Integer) 5);
    }
    @Test
    public void vendingMachineRejectsPennies() {
        vendingMachine.acceptCoins(1);

        assertEquals(vendingMachine.returnCoins, (Integer) 1);

    }
    @Test
    public void vendingMachineUpdatesDisplayWhenValidCoinsAccepted() {
        vendingMachine.acceptCoins(25);

        assertEquals(vendingMachine.display(), String.format("Current Amount: %d", vendingMachine.currentAmount));
    }
    @Test
    public void vendingMachineUpdatesDisplayWhenNoCoinsInserted() {
        assertEquals(vendingMachine.display(), "INSERT COINS");
    }
    @Test
    public void vendingMachineHasStock() {
        HashMap<String, Integer> products = new HashMap<>();
        products.put("Cola", 100);
        products.put("chips", 50);
        products.put("candy", 65);

        assertEquals(vendingMachine.products, products);
    }
}