import SwiftUI

/// Black ink on light grey, white cards. The same palette as LifeTrends.
enum Theme {
    static let background = Color(light: 0xF5F5F7, dark: 0x000000)
    static let card = Color(light: 0xFFFFFF, dark: 0x1C1C1E)
    static let ink = Color(light: 0x1D1D1F, dark: 0xF5F5F7)
    static let secondary = Color(light: 0x86868B, dark: 0x98989D)
    static let track = Color(light: 0xE8E8ED, dark: 0x2C2C2E)
    static let well = Color(light: 0xF2F2F4, dark: 0x2C2C2E)
}

extension Color {
    init(light: UInt32, dark: UInt32) {
        self.init(uiColor: UIColor { traits in
            UIColor(hex: traits.userInterfaceStyle == .dark ? dark : light)
        })
    }
}

extension UIColor {
    convenience init(hex: UInt32) {
        self.init(
            red: CGFloat((hex >> 16) & 0xFF) / 255,
            green: CGFloat((hex >> 8) & 0xFF) / 255,
            blue: CGFloat(hex & 0xFF) / 255,
            alpha: 1
        )
    }
}

struct Card: ViewModifier {
    var padding: CGFloat = 20

    func body(content: Content) -> some View {
        content
            .padding(padding)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(Theme.card, in: RoundedRectangle(cornerRadius: 22, style: .continuous))
            .shadow(color: .black.opacity(0.04), radius: 12, y: 2)
    }
}

extension View {
    func card(padding: CGFloat = 20) -> some View {
        modifier(Card(padding: padding))
    }
}
