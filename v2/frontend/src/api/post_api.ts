import { apiClient } from "./client";
import type { Post } from "../types/post";

export function createPost(text: string): Promise<Post> {
  return apiClient.post<Post>("/posts", { text });
}

export function likePost(postId: string): Promise<Post> {
  return apiClient.post<Post>(`/posts/${postId}/like`);
}

export function repostPost(postId: string): Promise<Post> {
  return apiClient.post<Post>(`/posts/${postId}/repost`);
}
