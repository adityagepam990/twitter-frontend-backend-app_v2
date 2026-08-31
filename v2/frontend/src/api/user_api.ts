import { apiClient } from "./client";
import type { User } from "../types/user";

export function fetchSuggestedUsers(): Promise<User[]> {
  return apiClient.get<User[]>("/users/suggested");
}

export function followUser(userId: string): Promise<User> {
  return apiClient.post<User>(`/users/${userId}/follow`);
}
