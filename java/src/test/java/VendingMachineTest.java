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

        assertEquals((Integer) 25, vendingMachine.currentAmount);
    }
    @Test
    public void vendingMachineAcceptsDimes() {
        vendingMachine.acceptCoins(10);

        assertEquals((Integer) 10, vendingMachine.currentAmount);
    }
    @Test
    public void vendingMachineAcceptsNickels() {
        vendingMachine.acceptCoins(5);

        assertEquals((Integer) 5, vendingMachine.currentAmount);
    }
    @Test
    public void vendingMachineRejectsPennies() {
        vendingMachine.acceptCoins(1);

        assertEquals((Integer) 1, vendingMachine.returnCoins());

    }
    @Test
    public void vendingMachineUpdatesDisplayWhenValidCoinsAccepted() {
        vendingMachine.acceptCoins(25);

        assertEquals(String.format("Current Amount: %d", vendingMachine.currentAmount), vendingMachine.display());
    }
    @Test
    public void vendingMachineUpdatesDisplayWhenNoCoinsInserted() {
        assertEquals("INSERT COINS", vendingMachine.display());
    }
    @Test
    public void vendingMachineHasStock() {
        HashMap<String, Integer> products = new HashMap<>();
        products.put("Cola", 100);
        products.put("Chips", 50);
        products.put("Candy", 65);

        assertEquals(products, vendingMachine.products);
    }
    @Test
    public void vendingMachineDispensesProductWhenFundsReceived() {
        for (int i = 0; i < 4; i++) {
            vendingMachine.acceptCoins(25);
        }
        assertEquals("Cola", vendingMachine.selectProduct("Cola"));
        assertEquals("THANK YOU", vendingMachine.display());

        assertEquals("INSERT COINS", vendingMachine.display());
        assertEquals((Integer) 0, vendingMachine.currentAmount);
    }
    @Test
    public void vendingMachineDisplaysPriceIfInsufficientFunds() {
        vendingMachine.selectProduct("Cola");

        assertEquals("PRICE: 100", vendingMachine.display());
        assertEquals("INSERT COINS", vendingMachine.display());
    }
    @Test
    public void vendingMachineDispensesProductAndReturnsExtraMoney() {
        for (int i = 0; i < 4; i++) {
            vendingMachine.acceptCoins(25);
        }

        assertEquals("Chips", vendingMachine.selectProduct("Chips"));
        assertEquals((Integer) 50, vendingMachine.returnCoins());
    }
    @Test
    public void vendingMachineReturnsCoins() {
        vendingMachine.acceptCoins(25);
        vendingMachine.refundCoins();

        assertEquals((Integer) 25, vendingMachine.returnCoins());
        assertEquals("INSERT COINS", vendingMachine.display());
    }
    @Test
    public void vendingMachineDisplaysSoldOutIfItemOutOfStock() {
        for (int i = 0; i < 4; i++) {
            vendingMachine.acceptCoins(25);
        }
        vendingMachine.selectProduct("cola");
        vendingMachine.selectProduct("cola");

        assertEquals("OUT OF STOCK", vendingMachine.display());
        assertEquals(String.format("Current Amount: %d", vendingMachine.currentAmount), vendingMachine.display());
    }
}