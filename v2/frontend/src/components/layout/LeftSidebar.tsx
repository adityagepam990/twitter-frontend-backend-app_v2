import {
  Bell,
  CircleEllipsis,
  Home,
  Mail,
  Search,
  Sparkles,
  Twitter,
  User,
  Users,
  Zap,
} from "lucide-react";

import { Avatar } from "../ui/Avatar";
import styles from "./LeftSidebar.module.scss";

interface NavItem {
  label: string;
  icon: typeof Home;
  active?: boolean;
}

const NAV_ITEMS: NavItem[] = [
  { label: "Home", icon: Home, active: true },
  { label: "Explore", icon: Search },
  { label: "Notifications", icon: Bell },
  { label: "Messages", icon: Mail },
  { label: "Grok", icon: Sparkles },
  { label: "Communities", icon: Users },
  { label: "Premium", icon: Zap },
  { label: "Verified Orgs", icon: Twitter },
  { label: "Profile", icon: User },
  { label: "More", icon: CircleEllipsis },
];

export function LeftSidebar() {
  return (
    <div className={styles.sidebar}>
      <div className={styles.logo}>
        <Twitter />
      </div>

      <nav className={styles.nav}>
        {NAV_ITEMS.map(({ label, icon: Icon, active }) => (
          <button
            key={label}
            type="button"
            className={active ? `${styles.navItem} ${styles.active}` : styles.navItem}
          >
            <Icon className={styles.navIcon} />
            <span className={styles.navLabel}>{label}</span>
          </button>
        ))}
      </nav>

      <button type="button" className={styles.postButton}>
        <span className={styles.postButtonLabel}>Post</span>
      </button>

      <div className={styles.account}>
        <Avatar src="" displayName="Pulse User" size="md" />
        <div className={styles.accountInfo}>
          <span className={styles.accountName}>Pulse User</span>
          <span className={styles.accountHandle}>@pulseuser</span>
        </div>
      </div>
    </div>
  );
}
