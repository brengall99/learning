import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Card } from "@/components/ui/card";
import { Stock } from '../types/stock';

interface PortfolioChartProps {
  stocks: Stock[];
  stockPrices: Record<string, number>;
}

export function PortfolioChart({ stocks, stockPrices }: PortfolioChartProps) {
  // Calculate total portfolio value over time
  const calculatePortfolioValue = () => {
    const now = new Date();
    const data = [];
    
    // Create data points for the last 7 days
    for (let i = 6; i >= 0; i--) {
      const date = new Date(now);
      date.setDate(date.getDate() - i);
      
      // Calculate portfolio value for this date
      const totalValue = stocks.reduce((sum, stock) => {
        const currentPrice = stockPrices[stock.symbol] || stock.purchasePrice;
        return sum + (currentPrice * stock.quantity);
      }, 0);

      data.push({
        date: date.toLocaleDateString(),
        value: totalValue
      });
    }
    
    return data;
  };

  const data = calculatePortfolioValue();

  return (
    <Card className="p-6 mb-8">
      <h2 className="text-xl font-semibold mb-4">Portfolio Value Over Time</h2>
      <div className="h-[300px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis 
              dataKey="date" 
              tick={{ fontSize: 12 }}
            />
            <YAxis 
              tick={{ fontSize: 12 }}
              tickFormatter={(value) => `$${value.toLocaleString()}`}
            />
            <Tooltip 
              formatter={(value: number) => [`$${value.toLocaleString()}`, 'Portfolio Value']}
            />
            <Line 
              type="monotone" 
              dataKey="value" 
              stroke="#1E3A8A" 
              strokeWidth={2}
              dot={{ fill: '#1E3A8A' }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </Card>
  );
}