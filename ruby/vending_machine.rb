require "byebug"

class VendingMachine

  attr_reader :current_amount, :purchased, :products, :coin_return, :coins, :basket, :out_of_stock
  attr_accessor :change

  def initialize
    # Maybe better to store as int for money
    @current_amount = 0.0
    @products = { "cola" => [1.00, 4], "chips" => [0.50, 5], "candy" => [0.65, 3] }
    @coins = { "quarter" => 0.25, "dime" => 0.10, "nickel" => 0.05 }
    @purchased = []
    @coin_return = []
    @basket = []
    @out_of_stock = []
    @change = 10.00
  end

  # Should be extracted to its own VendingDisplay object
  def display
    case
    when sold_out? && recently_out_of_stock? then "SOLD OUT"
    when sold_out? then price_display(@current_amount)
    when exact_change_only? then "EXACT CHANGE ONLY"
    when @current_amount.zero? && @purchased.length < 1 then "INSERT COINS"
    when recently_purchased? then "THANK YOU"
    when @current_amount > 0 then price_display(@current_amount)
    end
  end

  def price_display(value)
    "#{sprintf("%.2f", value)}"
  end

  def recently_out_of_stock?
    @last_seen > Time.now - 0.1
  end
  private "recently_out_of_stock?"

  def recently_purchased?
    @current_amount.zero? && @last_purchased > Time.now - 0.1
  end
  private "recently_purchased?"

  def exact_change_only?
    @change.zero?
  end
  private "exact_change_only?"

  def accept_coins(coin)
    if @coins[coin]
      @current_amount += @coins[coin]
    else
      @coin_return << coin
    end
  end

  def select_product(product)
    product_price = @products[product][0]
    product_quantity = @products[product][1]

    if @products[product] && product_quantity.nonzero?
      if @current_amount == product_price
        @purchased << product
        @products[product][1] -= 1
        @current_amount = 0.0
      elsif @current_amount < product_price
        @basket << [product, product_price]
      elsif @current_amount > product_price
        @purchased << product
        @products[product][1] -= 1
        @current_amount -= product_price
      end
      @last_purchased = Time.now
    elsif @products[product] && product_quantity.zero?
      @out_of_stock << [product, product_price]
      @products.delete(product)
      @last_seen = Time.now
    end
  end

  def sold_out?
    !@out_of_stock.empty?
  end
  private "sold_out?"

  def make_change
    customer_coin_return
  end

  def return_coins
    customer_coin_return
  end

  def customer_coin_return
    @coins.each do |coin_type, value|
      while @current_amount > 0.0
        if @current_amount -= value
          @coin_return << coin_type
        end
      end
    end
  end
  private "customer_coin_return"
end
