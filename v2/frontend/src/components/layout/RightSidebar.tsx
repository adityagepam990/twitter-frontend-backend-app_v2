import { useEffect } from "react";

import { useFeedStore } from "../../store/feed_store";
import { Avatar } from "../ui/Avatar";
import { FollowButton } from "../ui/FollowButton";
import styles from "./RightSidebar.module.scss";

export function RightSidebar() {
  const trends = useFeedStore((state) => state.trends);
  const suggestedUsers = useFeedStore((state) => state.suggestedUsers);
  const loadSidebar = useFeedStore((state) => state.loadSidebar);

  useEffect(() => {
    void loadSidebar();
  }, [loadSidebar]);

  return (
    <div className={styles.sidebar}>
      <input type="search" className={styles.search} placeholder="Search" />

      <section className={styles.card}>
        <h2 className={styles.cardTitle}>Subscribe to Premium</h2>
        <p className={styles.cardDescription}>
          Subscribe to unlock new features and, if eligible, receive a share of revenue.
        </p>
        <button type="button" className={styles.premiumButton}>
          Subscribe to Premium at ₹799/month
        </button>
      </section>

      <section className={styles.card}>
        <h2 className={styles.cardTitle}>Trends for you</h2>
        {trends.map((trend) => (
          <div key={trend.id} className={styles.trendRow}>
            <span className={styles.trendCategory}>{trend.category}</span>
            <span className={styles.trendTopic}>{trend.topic}</span>
            <span className={styles.trendCount}>{trend.post_count} posts</span>
          </div>
        ))}
      </section>

      <section className={styles.card}>
        <h2 className={styles.cardTitle}>Who to follow</h2>
        {suggestedUsers.map((user) => (
          <div key={user.id} className={styles.userRow}>
            <Avatar displayName={user.display_name} size="md" />
            <div className={styles.userInfo}>
              <span className={styles.userName}>{user.display_name}</span>
              <span className={styles.userHandle}>{user.handle}</span>
            </div>
            <FollowButton userId={user.id} followed={user.followed} />
          </div>
        ))}
      </section>
    </div>
  );
}
