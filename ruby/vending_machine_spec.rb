require_relative "vending_machine"

describe VendingMachine do
  let(:vending_machine) { VendingMachine.new }

  describe "#current_amount" do
    it "is readable" do
      expect(vending_machine.current_amount).to eq(0.0)
    end
  end
  describe "#purchased" do
    it "is readable" do
      expect(vending_machine.purchased).to eq([])
    end
  end

  describe "#products" do
    it "is readable" do
      vending_items =  { "cola" => [1.00, 4], "chips" => [0.50, 5], "candy" => [0.65, 3] }
      expect(vending_machine.products).to eq(vending_items)
    end
  end
  describe "#coin_return" do
    it "is readable" do
      expect(vending_machine.coin_return).to eq([])
    end
  end
  describe "#coins" do
    it "is readable" do
      coins = { "quarter" => 0.25, "dime" => 0.10, "nickel" => 0.05 }

      expect(vending_machine.coins).to eq(coins)
    end
  end
  describe "#basket" do
    it "is readable" do
      expect(vending_machine.basket).to eq([])
    end
  end
  describe "#out_of_stock" do
    it "is readable" do
      expect(vending_machine.out_of_stock).to eq([])
    end
  end
  describe "#change" do
    it "is readable" do
      expect(vending_machine.change).to eq(10.00)
    end
    it "is writeable" do
      vending_machine.change = 5.00
      expect(vending_machine.change).to eq(5.00)
    end
    it "displays EXACT CHANGE ONLY if cannot make change" do
      vending_machine.change -= 10.0

      expect(vending_machine.display).to eq("EXACT CHANGE ONLY")
    end
  end

  describe "#accept_coins" do
    context "accepts valid coins" do
      it "accepts quarters" do
        vending_machine.accept_coins("quarter")

        expect(vending_machine.current_amount).to eq(0.25)
        expect(vending_machine.display).to eq("0.25")
      end
      it "accepts dimes" do
        vending_machine.accept_coins("dime")

        expect(vending_machine.current_amount).to eq(0.10)
        expect(vending_machine.display).to eq("0.10")
      end
      it "accepts nickels" do
        vending_machine.accept_coins("nickel")

        expect(vending_machine.current_amount).to eq(0.05)
        expect(vending_machine.display).to eq("0.05")
      end
    end
    context "rejects invalid coins" do
      it "rejects pennies" do
        vending_machine.accept_coins("penny")

        expect(vending_machine.coin_return).to eq(["penny"])
      end
    end
    context "when no coins are inserted" do
      it "displays INSERT COINS" do
        expect(vending_machine.display).to eq("INSERT COINS")
      end
    end
  end

  describe "#select_product" do
      it "dispenses the products when enough money is inserted" do
      4.times { vending_machine.accept_coins("quarter") }
      vending_machine.select_product("cola")

      # vending machine would care that quantity has been reduced, not that an item has been purchased
      expect(vending_machine.purchased).to include("cola")
      expect(vending_machine.display).to eq("THANK YOU")
    end
    it "displays INSERT COIN if display is checked again" do
      expect(vending_machine.display).to eq("INSERT COINS")
    end
    it "does not dispense products when not enough money is inserted" do
      3.times { vending_machine.accept_coins("quarter") }
      products = ["cola", 1.00]

      vending_machine.select_product(products[0])

      # should expect that product quantity has not changed
      expect(vending_machine.price_display(products[1])).to eq("1.00")
      expect(vending_machine.display).to eq("0.75")
    end
    it "displays SOLD OUT if item is out of stock" do
        20.times { vending_machine.accept_coins("quarter") }
        5.times { vending_machine.select_product("cola") }

        expect(vending_machine.display).to eq("SOLD OUT")
    end
    it "second display when item is sold out is amount remaining or INSERT COIN" do
      20.times { vending_machine.accept_coins("quarter") }
      5.times { vending_machine.select_product("cola") }
      vending_machine.display

      # might not be the best way to go about it
      sleep(0.1)

      expect(vending_machine.display).to eq("1.00")
    end
  end

  describe "#make_change" do
    it "places remaining amount in coin return" do
      3.times { vending_machine.accept_coins("quarter") }
      vending_machine.make_change

      expect(vending_machine.coin_return).to eq(["quarter", "quarter", "quarter"])
    end
  end
  describe "#return_coins" do
    it "returns customer's money" do
      3.times { vending_machine.accept_coins("quarter") }
      vending_machine.return_coins

      expect(vending_machine.coin_return).to eq(["quarter", "quarter", "quarter"])
      expect(vending_machine.display).to eq("INSERT COINS")
    end
  end
end