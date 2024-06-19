import { useTheme, type ThemeInstance } from "vuetify"


export function toggleTheme(theme:ThemeInstance) {
    const isDark = theme.global.current.value.dark
    const color = isDark ? 'light' : 'dark'
    theme.global.name.value = color
    localStorage.setItem('weightbook-theme',color)
}

export function setThemeFromLocalStorage(theme:ThemeInstance) {
    const color = localStorage.getItem('weightbook-theme') ?? 'light'
    theme.global.name.value = color
}