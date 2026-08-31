import { useState } from "react";
import { BarChart2, Heart, MessageCircle, Repeat2, Share } from "lucide-react";

import { useFeedStore } from "../../store/feed_store";
import type { Post } from "../../types/post";
import styles from "./PostActions.module.scss";

interface PostActionsProps {
  post: Post;
}

export function PostActions({ post }: PostActionsProps) {
  const toggleLike = useFeedStore((state) => state.toggleLike);
  const toggleRepost = useFeedStore((state) => state.toggleRepost);
  const [isLiked, setIsLiked] = useState(false);
  const [isReposted, setIsReposted] = useState(false);

  const handleLike = () => {
    setIsLiked((current) => !current);
    void toggleLike(post.id);
  };

  const handleRepost = () => {
    setIsReposted((current) => !current);
    void toggleRepost(post.id);
  };

  return (
    <div className={styles.actions}>
      <button type="button" className={styles.action}>
        <MessageCircle className={styles.icon} />
        <span className={styles.count}>{post.reply_count}</span>
      </button>

      <button
        type="button"
        className={isReposted ? `${styles.action} ${styles.reposted}` : styles.action}
        onClick={handleRepost}
      >
        <Repeat2 className={styles.icon} />
        <span className={styles.count}>{post.repost_count}</span>
      </button>

      <button
        type="button"
        className={isLiked ? `${styles.action} ${styles.liked}` : styles.action}
        onClick={handleLike}
      >
        <Heart className={styles.icon} />
        <span className={styles.count}>{post.like_count}</span>
      </button>

      <button type="button" className={styles.action}>
        <BarChart2 className={styles.icon} />
      </button>

      <button type="button" className={styles.action}>
        <Share className={styles.icon} />
      </button>
    </div>
  );
}
