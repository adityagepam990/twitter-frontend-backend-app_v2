import { create } from "zustand";

import { fetchFeed, type FeedTab } from "../api/feed_api";
import { createPost, likePost, repostPost } from "../api/post_api";
import { fetchSuggestedUsers } from "../api/user_api";
import { fetchTrends } from "../api/trend_api";
import type { ApiError } from "../api/client";
import type { Post } from "../types/post";
import type { Trend } from "../types/trend";
import type { User } from "../types/user";

export type FeedStatus = "idle" | "loading" | "success" | "error";

export interface FeedState {
  posts: Post[];
  tab: FeedTab;
  suggestedUsers: User[];
  trends: Trend[];
  status: FeedStatus;
  error: string | null;
}

type FeedAction =
  | { type: "FEED_LOADING" }
  | { type: "FEED_LOADED"; posts: Post[] }
  | { type: "FEED_FAILED"; error: string }
  | { type: "TAB_SET"; tab: FeedTab }
  | { type: "SIDEBAR_LOADED"; suggestedUsers: User[]; trends: Trend[] }
  | { type: "POST_UPDATED"; post: Post };

function feedReducer(state: FeedState, action: FeedAction): FeedState {
  switch (action.type) {
    case "FEED_LOADING":
      return { ...state, status: "loading", error: null };
    case "FEED_LOADED":
      return { ...state, status: "success", posts: action.posts };
    case "FEED_FAILED":
      return { ...state, status: "error", error: action.error };
    case "TAB_SET":
      return { ...state, tab: action.tab };
    case "SIDEBAR_LOADED":
      return { ...state, suggestedUsers: action.suggestedUsers, trends: action.trends };
    case "POST_UPDATED":
      return {
        ...state,
        posts: state.posts.map((post) => (post.id === action.post.id ? action.post : post)),
      };
  }
}

function errorMessage(error: unknown): string {
  if (error && typeof error === "object" && "detail" in error) {
    return String((error as ApiError).detail);
  }
  return "Something went wrong.";
}

interface FeedStore extends FeedState {
  dispatch: (action: FeedAction) => void;
  loadFeed: (tab: FeedTab) => Promise<void>;
  setTab: (tab: FeedTab) => void;
  submitPost: (text: string) => Promise<void>;
  toggleLike: (postId: string) => Promise<void>;
  toggleRepost: (postId: string) => Promise<void>;
  loadSidebar: () => Promise<void>;
}

const initialState: FeedState = {
  posts: [],
  tab: "for-you",
  suggestedUsers: [],
  trends: [],
  status: "idle",
  error: null,
};

export const useFeedStore = create<FeedStore>((set, get) => ({
  ...initialState,

  dispatch: (action) => set((state) => feedReducer(state, action)),

  loadFeed: async (tab) => {
    get().dispatch({ type: "FEED_LOADING" });
    try {
      const posts = await fetchFeed(tab);
      get().dispatch({ type: "FEED_LOADED", posts });
    } catch (error) {
      get().dispatch({ type: "FEED_FAILED", error: errorMessage(error) });
    }
  },

  setTab: (tab) => {
    get().dispatch({ type: "TAB_SET", tab });
    void get().loadFeed(tab);
  },

  submitPost: async (text) => {
    try {
      await createPost(text);
      await get().loadFeed(get().tab);
    } catch (error) {
      get().dispatch({ type: "FEED_FAILED", error: errorMessage(error) });
    }
  },

  toggleLike: async (postId) => {
    try {
      const post = await likePost(postId);
      get().dispatch({ type: "POST_UPDATED", post });
    } catch (error) {
      get().dispatch({ type: "FEED_FAILED", error: errorMessage(error) });
    }
  },

  toggleRepost: async (postId) => {
    try {
      const post = await repostPost(postId);
      get().dispatch({ type: "POST_UPDATED", post });
    } catch (error) {
      get().dispatch({ type: "FEED_FAILED", error: errorMessage(error) });
    }
  },

  loadSidebar: async () => {
    try {
      const [suggestedUsers, trends] = await Promise.all([fetchSuggestedUsers(), fetchTrends()]);
      get().dispatch({ type: "SIDEBAR_LOADED", suggestedUsers, trends });
    } catch (error) {
      get().dispatch({ type: "FEED_FAILED", error: errorMessage(error) });
    }
  },
}));
