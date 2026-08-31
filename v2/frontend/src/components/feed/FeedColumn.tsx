import { useEffect } from "react";

import { useFeedStore } from "../../store/feed_store";
import { FeedTabs } from "./FeedTabs";
import { PostCard } from "./PostCard";
import styles from "./FeedColumn.module.scss";

export function FeedColumn() {
  const posts = useFeedStore((state) => state.posts);
  const status = useFeedStore((state) => state.status);
  const error = useFeedStore((state) => state.error);
  const tab = useFeedStore((state) => state.tab);
  const loadFeed = useFeedStore((state) => state.loadFeed);

  useEffect(() => {
    void loadFeed(tab);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className={styles.column}>
      <FeedTabs />

      {status === "loading" && <div className={styles.state}>Loading feed…</div>}

      {status === "error" && <div className={styles.state}>{error ?? "Something went wrong."}</div>}

      {status === "success" && posts.length === 0 && (
        <div className={styles.state}>Nothing here yet.</div>
      )}

      {status === "success" && posts.length > 0 && (
        <div className={styles.list}>
          {posts.map((post) => (
            <PostCard key={post.id} post={post} />
          ))}
        </div>
      )}
    </div>
  );
}
