<template>
    <dev class="frame">
    <button v-bind="$attrs" class="button is-warning" size="small"> {{ buttonText }} </button>
    </dev>
</template>

<script>
export default {
    props: {
        buttonText: {
            type: String,
            default: () => "<ButtonName>",
        }
    }
};
</script>


<style scoped>
    .frame {
        margin-left: 5px;
    }
</style>