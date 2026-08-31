export interface Post {
  id: string;
  author_id: string;
  author_name: string;
  author_handle: string;
  author_avatar_url: string;
  author_followed: boolean;
  body: string;
  created_at: string;
  reply_count: number;
  repost_count: number;
  like_count: number;
  image_url: string | null;
}
