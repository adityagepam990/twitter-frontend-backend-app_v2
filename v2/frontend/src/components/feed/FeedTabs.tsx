import type { FeedTab } from "../../api/feed_api";
import { useFeedStore } from "../../store/feed_store";
import styles from "./FeedTabs.module.scss";

const TABS: { tab: FeedTab; label: string }[] = [
  { tab: "for-you", label: "For You" },
  { tab: "following", label: "Following" },
];

export function FeedTabs() {
  const activeTab = useFeedStore((state) => state.tab);
  const setTab = useFeedStore((state) => state.setTab);

  return (
    <div className={styles.tabs}>
      {TABS.map(({ tab, label }) => (
        <button
          key={tab}
          type="button"
          className={tab === activeTab ? `${styles.tab} ${styles.active}` : styles.tab}
          onClick={() => setTab(tab)}
        >
          {label}
        </button>
      ))}
    </div>
  );
}
