import { apiClient } from "./client";
import type { Trend } from "../types/trend";

export function fetchTrends(): Promise<Trend[]> {
  return apiClient.get<Trend[]>("/trends");
}
