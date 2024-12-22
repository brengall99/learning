export interface Stock {
  id: string;
  symbol: string;
  quantity: number;
  purchaseDate: string;
  purchasePrice: number;
  alerts: number[];
  currentPrice?: number;
  priceChange?: number;
}