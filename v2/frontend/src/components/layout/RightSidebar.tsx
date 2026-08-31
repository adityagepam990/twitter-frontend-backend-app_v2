import styles from "./RightSidebar.module.scss";

export function RightSidebar() {
  return (
    <div className={styles.sidebar}>
      <input type="search" className={styles.search} placeholder="Search" />

      <section className={styles.card}>
        <h2 className={styles.cardTitle}>Subscribe to Premium</h2>
        <div className={styles.skeletonLine} />
        <div className={styles.skeletonLine} />
        <div className={styles.skeletonButton} />
      </section>

      <section className={styles.card}>
        <h2 className={styles.cardTitle}>Trends for you</h2>
        {[0, 1, 2].map((index) => (
          <div key={index} className={styles.skeletonRow}>
            <div className={styles.skeletonLine} />
            <div className={styles.skeletonLineShort} />
          </div>
        ))}
      </section>

      <section className={styles.card}>
        <h2 className={styles.cardTitle}>Who to follow</h2>
        {[0, 1, 2].map((index) => (
          <div key={index} className={styles.skeletonRow}>
            <div className={styles.skeletonAvatar} />
            <div className={styles.skeletonLine} />
          </div>
        ))}
      </section>
    </div>
  );
}
