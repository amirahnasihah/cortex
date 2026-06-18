# Tailwind CSS - Transitions & Animation


## Transition Property

| ** Class** | **Styles** |
 | `transition` `transition-property: color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events;
transition-timing-function: var(--default-transition-timing-function); /* cubic-bezier(0.4, 0, 0.2, 1) */
transition-duration: var(--default-transition-duration); /* 150ms */ `

## Transition Behavior

| ** Class** | **Styles** |
 | `transition-normal` `transition-behavior: normal;`

## Transition Duration

| ** Class** | **Styles** |
 | `duration- <number> ` `transition-duration: <number> ms;`

## Transition Timing Function

| ** Class** | **Styles** |
 | `ease-linear` `transition-timing-function: linear;`

## Transition Delay

| ** Class** | **Styles** |
 | `delay- <number> ` `transition-delay: <number> ms;`

## Animation

| ** Class** | **Styles** |
 | `animate-spin` `animation: var(--animate-spin); /* spin 1s linear infinite */

@keyframes spin {
 to {
 transform: rotate(360deg);
 }
}`