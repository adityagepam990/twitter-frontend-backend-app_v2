import type { Post } from "../../types/post";
import { Avatar } from "../ui/Avatar";
import { PostActions } from "./PostActions";
import styles from "./PostCard.module.scss";

interface PostCardProps {
  post: Post;
}

function formatRelativeTime(createdAt: string): string {
  const elapsedMs = Date.now() - new Date(createdAt).getTime();
  const elapsedSeconds = Math.max(0, Math.floor(elapsedMs / 1000));

  if (elapsedSeconds < 60) {
    return `${elapsedSeconds}s`;
  }
  const elapsedMinutes = Math.floor(elapsedSeconds / 60);
  if (elapsedMinutes < 60) {
    return `${elapsedMinutes}m`;
  }
  const elapsedHours = Math.floor(elapsedMinutes / 60);
  if (elapsedHours < 24) {
    return `${elapsedHours}h`;
  }
  const elapsedDays = Math.floor(elapsedHours / 24);
  return `${elapsedDays}d`;
}

export function PostCard({ post }: PostCardProps) {
  return (
    <article className={styles.card}>
      <Avatar src={post.author_avatar_url} displayName={post.author_name} size="md" />

      <div className={styles.body}>
        <header className={styles.header}>
          <span className={styles.authorName}>{post.author_name}</span>
          <span className={styles.authorHandle}>@{post.author_handle}</span>
          <span className={styles.dot}>·</span>
          <span className={styles.timestamp}>{formatRelativeTime(post.created_at)}</span>
        </header>

        <p className={styles.text}>{post.body}</p>

        {post.image_url && (
          <img className={styles.image} src={post.image_url} alt="" />
        )}

        <PostActions post={post} />
      </div>
    </article>
  );
}
