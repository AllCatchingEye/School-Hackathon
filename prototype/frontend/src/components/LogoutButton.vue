<template>
    <dev class="frame">
    <button onclick="location.href='/logout'" v-bind="$attrs" class="button logout" size="small"> {{ buttonText }} </button>
    </dev>
</template>

<script>
export default {
    props: {
        buttonText: {
            type: String,
            default: () => "Abmelden",
        }
    }
};
</script>


<style scoped>
    .frame {
        margin-left: 5px;
    }
</style>