import { useState, useEffect } from "react";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Plus, Bell, Trash2, TrendingUp } from "lucide-react";
import { useToast } from "@/components/ui/use-toast";
import { useQuery } from "@tanstack/react-query";
import { PortfolioChart } from "./PortfolioChart";
import { Stock } from "../types/stock";

const fetchStockPrice = async (symbol: string) => {
  console.log(`Fetching price for ${symbol}`);
  try {
    const response = await fetch(
      `https://api.twelvedata.com/price?symbol=${symbol}&apikey=demo`
    );
    const data = await response.json();
    console.log(`Price data for ${symbol}:`, data);
    return parseFloat(data.price);
  } catch (error) {
    console.error(`Error fetching price for ${symbol}:`, error);
    return null;
  }
};

export function Portfolio() {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [newStock, setNewStock] = useState({
    symbol: "",
    quantity: "",
    purchaseDate: "",
    purchasePrice: "",
  });
  const { toast } = useToast();

  // Query for fetching stock prices
  const { data: stockPrices } = useQuery({
    queryKey: ['stockPrices', stocks.map(s => s.symbol)],
    queryFn: async () => {
      const prices: Record<string, number> = {};
      for (const stock of stocks) {
        const price = await fetchStockPrice(stock.symbol);
        if (price) prices[stock.symbol] = price;
      }
      return prices;
    },
    refetchInterval: 60000, // Refetch every minute
    enabled: stocks.length > 0,
  });

  // Update stocks with current prices
  useEffect(() => {
    if (stockPrices) {
      setStocks(stocks.map(stock => ({
        ...stock,
        currentPrice: stockPrices[stock.symbol],
        priceChange: stockPrices[stock.symbol] 
          ? ((stockPrices[stock.symbol] - stock.purchasePrice) / stock.purchasePrice) * 100
          : 0
      })));
    }
  }, [stockPrices]);

  const handleAddStock = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newStock.symbol || !newStock.quantity || !newStock.purchaseDate || !newStock.purchasePrice) {
      toast({
        title: "Error",
        description: "Please fill in all fields",
        variant: "destructive",
      });
      return;
    }

    const stock: Stock = {
      id: Date.now().toString(),
      symbol: newStock.symbol.toUpperCase(),
      quantity: Number(newStock.quantity),
      purchaseDate: newStock.purchaseDate,
      purchasePrice: Number(newStock.purchasePrice),
      alerts: [],
    };

    setStocks([...stocks, stock]);
    setNewStock({ symbol: "", quantity: "", purchaseDate: "", purchasePrice: "" });
    toast({
      title: "Success",
      description: `Added ${stock.quantity} shares of ${stock.symbol}`,
    });
  };

  const handleAddAlert = (stockId: string, price: string) => {
    if (!price) return;
    setStocks(
      stocks.map((stock) =>
        stock.id === stockId
          ? { ...stock, alerts: [...stock.alerts, Number(price)] }
          : stock
      )
    );
    toast({
      title: "Alert Set",
      description: `You will be notified when ${stocks.find((s) => s.id === stockId)?.symbol} reaches $${price}`,
    });
  };

  const handleRemoveStock = (id: string) => {
    setStocks(stocks.filter((stock) => stock.id !== id));
    toast({
      title: "Stock Removed",
      description: "The stock has been removed from your portfolio",
    });
  };

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-8">Stock Portfolio</h1>
      
      {stocks.length > 0 && stockPrices && (
        <PortfolioChart stocks={stocks} stockPrices={stockPrices} />
      )}

      <Card className="p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Add New Stock</h2>
        <form onSubmit={handleAddStock} className="flex flex-wrap gap-4">
          <Input
            placeholder="Stock Symbol (e.g., AAPL)"
            value={newStock.symbol}
            onChange={(e) => setNewStock({ ...newStock, symbol: e.target.value })}
            className="w-full sm:w-auto"
          />
          <Input
            type="number"
            placeholder="Quantity"
            value={newStock.quantity}
            onChange={(e) => setNewStock({ ...newStock, quantity: e.target.value })}
            className="w-full sm:w-auto"
          />
          <Input
            type="date"
            value={newStock.purchaseDate}
            onChange={(e) => setNewStock({ ...newStock, purchaseDate: e.target.value })}
            className="w-full sm:w-auto"
          />
          <Input
            type="number"
            step="0.01"
            placeholder="Purchase Price"
            value={newStock.purchasePrice}
            onChange={(e) => setNewStock({ ...newStock, purchasePrice: e.target.value })}
            className="w-full sm:w-auto"
          />
          <Button type="submit" className="w-full sm:w-auto">
            <Plus className="w-4 h-4 mr-2" /> Add Stock
          </Button>
        </form>
      </Card>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {stocks.map((stock) => (
          <Card key={stock.id} className="p-6">
            <div className="flex justify-between items-start mb-4">
              <div>
                <h3 className="text-2xl font-bold">{stock.symbol}</h3>
                <p className="text-gray-600">
                  {stock.quantity} shares @ ${stock.purchasePrice}
                </p>
                <p className="text-sm text-gray-500">
                  Purchased: {new Date(stock.purchaseDate).toLocaleDateString()}
                </p>
                {stock.currentPrice && (
                  <div className="mt-2">
                    <p className="text-lg font-semibold flex items-center gap-2">
                      Current: ${stock.currentPrice.toFixed(2)}
                      <span className={`text-sm ${stock.priceChange >= 0 ? 'text-green-500' : 'text-red-500'}`}>
                        <TrendingUp className={`w-4 h-4 inline ${stock.priceChange >= 0 ? '' : 'transform rotate-180'}`} />
                        {stock.priceChange.toFixed(2)}%
                      </span>
                    </p>
                  </div>
                )}
              </div>
              <Button
                variant="ghost"
                size="icon"
                onClick={() => handleRemoveStock(stock.id)}
              >
                <Trash2 className="w-4 h-4 text-gray-500" />
              </Button>
            </div>

            <div className="mt-4">
              <div className="flex items-center gap-2">
                <Input
                  type="number"
                  step="0.01"
                  placeholder="Alert Price"
                  className="flex-1"
                  onKeyPress={(e) => {
                    if (e.key === "Enter") {
                      handleAddAlert(stock.id, (e.target as HTMLInputElement).value);
                      (e.target as HTMLInputElement).value = "";
                    }
                  }}
                />
                <Button variant="outline" size="icon">
                  <Bell className="w-4 h-4" />
                </Button>
              </div>
              {stock.alerts.length > 0 && (
                <div className="mt-2">
                  <p className="text-sm text-gray-600">Price Alerts:</p>
                  <div className="flex flex-wrap gap-2 mt-1">
                    {stock.alerts.map((price, index) => (
                      <span
                        key={index}
                        className="px-2 py-1 text-sm bg-gray-100 rounded"
                      >
                        ${price}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
}
