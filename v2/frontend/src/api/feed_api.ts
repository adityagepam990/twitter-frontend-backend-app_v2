import { apiClient } from "./client";
import type { Post } from "../types/post";

export type FeedTab = "for-you" | "following";

export function fetchFeed(tab: FeedTab): Promise<Post[]> {
  return apiClient.get<Post[]>(`/feed?tab=${tab}`);
}
